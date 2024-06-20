import Vue from "vue"; // Import Vue framework
import App from "./App.vue"; // Import the main App component

// Create a new Vue instance
new Vue({
  render: h => h(App), // Render the App component into the root div
}).$mount("#app"); // Mount the Vue instance to the div with id "app" in the HTML file
