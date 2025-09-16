<template>
  <div class="container">
    <section class="skills">
      <h2 class="section-header">Skills</h2>
      <ul class="skills-list">
        <li>JavaScript</li>
        <li>Vue.js</li>
        <li>HTML5 & CSS3</li>
        <li>[Your other skills]</li>
      </ul>
    </section>
  </div>
</template>

<script>
export default {
  name: 'SkillsPage',
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