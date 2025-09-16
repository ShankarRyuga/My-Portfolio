<template>
  <div class="container">
    <section class="projects">
      <h2 class="section-header">Projects</h2>
      <div class="project-list">
        <div class="project-card">
          <h3>[Project Title]</h3>
          <p>[Brief description of the project. What did it do? What technologies did you use?]</p>
          <a href="[Link to GitHub or live demo]" target="_blank">View Project</a>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'ProjectsPage',
};
</script>

<style scoped>
.section-header {
  background-color: #b4c0cc;
  color: #333;
  padding: 0.8rem 2rem;
  border-radius: 8px;
  width: 100%;
  text-align: center;
  margin-bottom: 2rem;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
}
</style>