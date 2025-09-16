<template>
  <header class="header">
    <nav>
      <router-link to="/">About</router-link>
      <router-link to="/education">Education</router-link>
      <router-link to="/projects">Projects</router-link>
      <router-link to="/skills">Skills</router-link>
      <router-link to="/contact">Contact</router-link>
    </nav>
  </header>
</template>

<script>
export default {
  name: 'AppHeader',
};
</script>

<style scoped>
.header {
  background-color: #007bff;
  padding: 1.5rem 0;
  text-align: center;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  border-bottom-left-radius: 15px;
  border-bottom-right-radius: 15px;
}

.header nav a {
  margin: 0 1.5rem;
  text-decoration: none;
  color: white;
  font-weight: bold;
  font-size: 1.1rem;
  transition: color 0.3s, border-bottom 0.3s;
}

.header nav a:hover {
  color: #e9ecef;
}

.router-link-active {
  color: #ffffff;
  border-bottom: 2px solid #ffffff;
}
</style>