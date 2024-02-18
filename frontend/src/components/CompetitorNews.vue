<script setup lang="ts">
import { ref, onMounted, watch } from 'vue';
import DataService from './DataService.js';

const selectedTimeRange = ref('7d');
const items = ref([])

const fetchData = async () => {
  try {
    const response = await DataService.getData(selectedTimeRange.value );
    items.value = response.items;
  }catch(error){
    console.error(error);
  }
};

const selectTimeRange = async (range:string) => {
  selectedTimeRange.value = range;
};

selectTimeRange('30d')

onMounted(fetchData);

watch(selectedTimeRange, fetchData);
</script>

<template>
  <div class="homepage">
    <h1>Competitor News</h1>
    <hr>
    <div class="button-group">
      <label class="bold-label">Time Range:</label>
      <button @click="selectTimeRange('1d')" class="button">Today</button>
      <button @click="selectTimeRange('7d')" class="button">Last Week</button>
      <button @click="selectTimeRange('30d')" class="button">Last Month</button>
    </div>
    <table class="custom-table">
      <thead>
        <tr>
          <th style="width: 5%;">ID</th>
          <th style="width: 45%;">Title</th>
          <th style="width: 5%;">Level</th>
          <th style="width: 15%;">Publisher</th>
          <th style="width: 30%;">Published Date</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, index) in items" :key="index">
          <td>{{ index + 1 }}</td>
          <td>{{ item.title }}</td>
          <td>{{ item.level }}</td>
          <td><a :href="item.url">{{ item.publisher }}</a></td>
          <td>{{ item.published_date }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped>
.bold-label {
  font-weight: bold; 
}
.button-group {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

.button-group label {
  margin-right: 10px;
}

.button-group button {
  margin-right: 30px;
  background-color: lightgreen;
}
.custom-table {
  width: 100%;
  table-layout: fixed;
  border-collapse: collapse;
}

.custom-table th, .custom-table td {
  border: 1px solid #ddd;
  padding: 8px;
  /* white-space: nowrap;  */
  overflow: hidden; 
  text-overflow: ellipsis; 
}

.custom-table th {
  background-color: #f2f2f2;
}

.custom-table tbody tr:nth-child(even) {
  background-color: #f2f2f2;
}

hr {
  border: 0;
  height: 3px;
  background-color: #cccccc;
  margin: 10px 0;
}

</style>
