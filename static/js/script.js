/* ============================================================
   AssignTrack — script.js
   Uses jQuery for:
   - Form validation
   - DOM manipulation (show/hide elements)
   - Event handling (filter buttons, search, delete confirm)
   - Small UI effects
   ============================================================ */

$(document).ready(function () {

  // ── 1. FORM VALIDATION (jQuery) ──────────────────────────────
  // Triggered when Add Assignment form is submitted
  $("#addForm").on("submit", function (e) {
    let valid = true;

    // Check Title field
    if ($("#title").val().trim() === "") {
      $("#title").addClass("is-invalid");
      valid = false;
    } else {
      $("#title").removeClass("is-invalid");
    }

    // Check Subject field
    if ($("#subject").val().trim() === "") {
      $("#subject").addClass("is-invalid");
      valid = false;
    } else {
      $("#subject").removeClass("is-invalid");
    }

    // Check Due Date field
    if ($("#due_date").val() === "") {
      $("#due_date").addClass("is-invalid");
      valid = false;
    } else {
      $("#due_date").removeClass("is-invalid");
    }

    // If any field is empty, stop form submission
    if (!valid) {
      e.preventDefault();
    }
  });

  // Remove red border as soon as user starts typing
  $("#addForm input, #addForm select").on("input change", function () {
    $(this).removeClass("is-invalid");
  });


  // ── 2. DELETE CONFIRMATION (jQuery event handling) ───────────
  // When delete button is clicked, ask user to confirm
  $(".delete-btn").on("click", function (e) {
    const confirmed = confirm("Are you sure you want to delete this assignment?");
    if (!confirmed) {
      e.preventDefault();  // Stop navigation if user clicks Cancel
    }
  });


  // ── 3. FILTER BUTTONS (jQuery DOM manipulation) ──────────────
  // Show only rows that match the selected filter
  $(".filter-btn").on("click", function () {

    // Update active button style
    $(".filter-btn").removeClass("active btn-primary btn-warning btn-success btn-danger")
                    .addClass("btn-outline-secondary");
    $(this).removeClass("btn-outline-secondary").addClass("active btn-primary");

    const filter = $(this).data("filter");  // "all", "pending", "completed", "urgent"
    let visibleCount = 0;

    $(".assign-row").each(function () {
      const status   = $(this).data("status");
      const priority = $(this).data("priority");

      let show = false;
      if (filter === "all")       show = true;
      if (filter === "pending"  && status === "pending")                     show = true;
      if (filter === "completed"&& status === "completed")                   show = true;
      if (filter === "urgent"   && priority === "High" && status === "pending") show = true;

      // jQuery show/hide
      if (show) {
        $(this).show();
        visibleCount++;
      } else {
        $(this).hide();
      }
    });

    // Show "no results" message if nothing matches
    if (visibleCount === 0) {
      $("#noResults").removeClass("d-none");
    } else {
      $("#noResults").addClass("d-none");
    }
  });


  // ── 4. LIVE SEARCH (jQuery input event) ──────────────────────
  // Filter rows as user types in search box
  $("#searchInput").on("input", function () {
    const query = $(this).val().toLowerCase().trim();
    let visibleCount = 0;

    $(".assign-row").each(function () {
      const title   = $(this).data("title")   || "";
      const subject = $(this).data("subject") || "";

      if (title.includes(query) || subject.includes(query)) {
        $(this).show();
        visibleCount++;
      } else {
        $(this).hide();
      }
    });

    // Show "no results" message
    if (visibleCount === 0 && query !== "") {
      $("#noResults").removeClass("d-none");
    } else {
      $("#noResults").addClass("d-none");
    }
  });


  // ── 5. AUTO-DISMISS FLASH ALERTS after 4 seconds ─────────────
  setTimeout(function () {
    $(".alert").fadeOut(600, function () {
      $(this).remove();
    });
  }, 4000);


  // ── 6. HIGHLIGHT OVERDUE ROWS (jQuery DOM manipulation) ──────
  // Due date is stored as YYYY-MM-DD in data attribute
  const today = new Date().toISOString().split("T")[0];  // "2025-06-20"

  $(".assign-row").each(function () {
    const due    = $(this).find("td:nth-child(3)").text().trim();
    const status = $(this).data("status");

    if (status === "pending" && due < today) {
      // Add a light red background to overdue rows
      $(this).addClass("table-danger");
    }
  });

});