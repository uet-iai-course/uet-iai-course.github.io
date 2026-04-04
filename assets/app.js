(function () {
  var courses = Array.isArray(window.COURSES) ? window.COURSES : [];
  var courseGrid = document.getElementById("course-grid");

  if (!courseGrid) return;

  if (courses.length === 0) {
    courseGrid.innerHTML = '<p class="empty-state">Chưa có học phần nào được khai báo.</p>';
    return;
  }

  // Group by year
  var byYear = {};
  courses.forEach(function (course) {
    if (!byYear[course.year]) byYear[course.year] = [];
    byYear[course.year].push(course);
  });

  var yearLabels = { 1: "Năm nhất", 2: "Năm hai", 3: "Năm ba", 4: "Năm tư" };

  Object.keys(byYear).sort().forEach(function (year) {
    var yearGroup = document.createElement("div");
    yearGroup.className = "year-group";

    var yearHeading = document.createElement("h3");
    yearHeading.className = "year-heading";
    yearHeading.textContent = yearLabels[year] || "Năm " + year;
    yearGroup.appendChild(yearHeading);

    var semGrid = document.createElement("div");
    semGrid.className = "sem-grid";

    var bySem = {};
    byYear[year].forEach(function (c) { bySem[c.semester] = c; });

    [1, 2].forEach(function (sem) {
      var col = document.createElement("div");
      col.className = "sem-col";

      var semLabel = document.createElement("p");
      semLabel.className = "sem-label";
      semLabel.textContent = "Học kỳ " + sem;
      col.appendChild(semLabel);

      var course = bySem[sem];
      if (course) {
        var card = document.createElement("article");
        card.className = "course-card";

        var header = document.createElement("div");
        header.className = "course-header";

        var title = document.createElement("h4");
        title.textContent = course.title;

        var subtitle = document.createElement("p");
        subtitle.className = "course-subtitle";
        subtitle.textContent = course.englishTitle;

        header.appendChild(title);
        header.appendChild(subtitle);

        var courseLink = document.createElement("a");
        courseLink.className = "button button-secondary";
        courseLink.href = course.courseUrl;
        courseLink.textContent = "Xem tài liệu";

        card.appendChild(header);
        card.appendChild(courseLink);
        col.appendChild(card);
      }

      semGrid.appendChild(col);
    });

    yearGroup.appendChild(semGrid);
    courseGrid.appendChild(yearGroup);
  });
})();
