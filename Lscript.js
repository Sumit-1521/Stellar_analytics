// document.addEventListener("DOMContentLoaded", function () {
//     setTimeout(() => {
//         // Apply fade-out effect to the loader
//         document.querySelector(".content").classList.add("fade-out");

//         setTimeout(() => {
//             document.querySelector(".content").style.display = "none";
//             document.getElementById("homepage").style.display = "block";

//             setTimeout(() => {
//                 document.getElementById("homepage").classList.remove("hidden");
//             }, 100);
//         }, 1500); // Wait for fade-out to complete before hiding
//     }, 5000); // Loader duration
// });


// document.addEventListener("DOMContentLoaded", function () {
//     let df_planets, df_ranking, df_merged;

//     // Load CSV Files
//     Promise.all([
//         d3.csv("Preprocessed_Planet_Data.csv"),
//         d3.csv("Final_Habitability_Data.csv")
//     ]).then(function (data) {
//         df_planets = data[0];
//         df_ranking = data[1];

//         // Merge data
//         df_merged = df_planets.map(planet => {
//             let ranking = df_ranking.find(r => r["Planet Name"] === planet["P_NAME"]);
//             return ranking ? { ...planet, ...ranking } : null;
//         }).filter(p => p !== null);

//         populateFilters();
//         updateDashboard();
//     });

//     function populateFilters() {
//         let habitabilityOptions = [...new Set(df_merged.map(p => p["Habitability_Category"]))];
//         let habitabilitySelect = document.getElementById("habitabilityFilter");
        
//         habitabilityOptions.forEach(option => {
//             let opt = document.createElement("option");
//             opt.value = option;
//             opt.textContent = option;
//             habitabilitySelect.appendChild(opt);
//         });

//         let planetSelect = document.getElementById("planetSelect");
//         df_merged.forEach(planet => {
//             let opt = document.createElement("option");
//             opt.value = planet["P_NAME"];
//             opt.textContent = planet["P_NAME"];
//             planetSelect.appendChild(opt);
//         });

//         habitabilitySelect.addEventListener("change", updateDashboard);
//         planetSelect.addEventListener("change", showPlanetDetails);
//     }

//     function updateDashboard() {
//         let filteredData = df_merged;

//         // Metrics
//         document.getElementById("totalPlanets").textContent = filteredData.length;
//         document.getElementById("habitablePlanets").textContent = filteredData.filter(p => p["P_HABITABLE"] === "1").length;
//         document.getElementById("avgHabitability").textContent = 
//             (filteredData.reduce((sum, p) => sum + parseFloat(p["Habitability Index"]), 0) / filteredData.length).toFixed(2);

//         // Charts
//         let habitabilityCounts = {};
//         filteredData.forEach(p => {
//             habitabilityCounts[p["Habitability_Category"]] = (habitabilityCounts[p["Habitability_Category"]] || 0) + 1;
//         });

//         Plotly.newPlot("habitabilityPie", [{
//             values: Object.values(habitabilityCounts),
//             labels: Object.keys(habitabilityCounts),
//             type: "pie"
//         }]);

//         let scatterData = {
//             x: filteredData.map(p => p["Global ESI"]),
//             y: filteredData.map(p => p["Habitability Index"]),
//             mode: "markers",
//             type: "scatter",
//             text: filteredData.map(p => p["P_NAME"]),
//             marker: { size: 10, color: "blue" }
//         };
//         Plotly.newPlot("scatterChart", [scatterData]);
//     }

//     function showPlanetDetails() {
//         let selectedPlanet = document.getElementById("planetSelect").value;
//         let planet = df_merged.find(p => p["P_NAME"] === selectedPlanet);

//         document.getElementById("planetDetails").innerHTML = `
//             <p><b>Mass:</b> ${planet["P_MASS"]} Earth masses</p>
//             <p><b>Radius:</b> ${planet["P_RADIUS"]} Earth radii</p>
//             <p><b>Temperature:</b> ${planet["P_TEMP_SURF"]} K</p>
//             <p><b>Gravity:</b> ${planet["P_GRAVITY"]} m/s²</p>
//             <p><b>Global ESI:</b> ${planet["Global ESI"]}</p>
//             <p><b>Habitability Index:</b> ${planet["Habitability Index"]}</p>
//         `;
//     }
// });


setTimeout(function() {
    window.location.href = "http://localhost:8501"; // Redirects to Streamlit
}, 10000); // 10 seconds delay


