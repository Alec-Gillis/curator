<template>
  <div>
    <button @click="login">Login with Spotify</button>
    <div v-if="username">Logged in as: {{ username }}</div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: null,
    };
  },
  methods: {
    async login() {
      window.location.href = "http://localhost:8000/auth/login";
    },
    async fetchUser() {
      const response = await fetch("http://localhost:8000/api/user");
      const data = await response.json();
      this.username = data.username;
    },
  },
  mounted() {
    this.fetchUser();
  },
};
</script>
