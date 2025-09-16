<template>
  <div class="container">
    <section class="education">
      <h2 class="section-header">Education</h2>
      <ul>
        <li>
          <h3>[University Name]</h3>
          <p>[Degree], [Field of Study]</p>
          <p>[Start Date] - [End Date]</p>
        </li>
      </ul>
    </section>
  </div>
</template>

<script>
export default {
  name: 'EducationPage',
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