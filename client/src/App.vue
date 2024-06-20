<template>
  <div>
    <!-- Button to trigger Spotify login -->
    <button @click="login">Login with Spotify</button>
    <!-- Display the username if the user is logged in -->
    <div v-if="username">Logged in as: {{ username }}</div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: null, // Initialize username data property to null
    };
  },
  methods: {
    // Method to redirect the user to the Spotify login page
    async login() {
      window.location.href = "http://localhost:8000/auth/login";
    },
    // Method to fetch the logged-in user's information from the backend
    async fetchUser() {
      const response = await fetch("http://localhost:8000/api/user"); // Fetch user data from the backend
      const data = await response.json(); // Parse the JSON response
      this.username = data.username; // Set the username data property
    },
  },
  // Fetch the user information when the component is mounted
  mounted() {
    this.fetchUser();
  },
};
</script>
