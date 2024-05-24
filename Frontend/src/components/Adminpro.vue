<template>
    <div class="min-h-screen flex">
      <Admindash />
      <div class="flex-grow p-6">
        <div class="bg-white rounded-lg p-6">
          <p class="text-3xl text-center my-10 text-lightblue">Admin Profile</p>
          <table class="w-2/3 border-collapse ml-64 mt-10">
            <thead>
              <tr class="border-4 border-purple text-xl text-center">
                <th class="p-3">Email</th>
                <th class="p-3">Date of Birth</th>
                <th class="p-3">Country</th>
                <th class="p-3">Bio</th>
                <th class="p-3">Gender</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="artist in artists" :key="artist.id" class="border-4 border-purple text-center">
                <template v-if="artist.is_superuser">
                  <td class="p-3">{{ artist.email }}</td>
                  <td class="p-3">{{ artist.dob }}</td>
                  <td class="p-3">{{ artist.country }}</td>
                  <td class="p-3">{{ artist.bio }}</td>
                  <td class="p-3">{{ artist.gender }}</td>
                </template>
              </tr>
            </tbody>
          </table>

        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import axios from 'axios';
  import Admindash from './Admindash.vue';
  
  const artists = ref([]);
  
  onMounted(async () => {
    try {
      const accessToken = localStorage.getItem('accessToken');
      const response = await axios.get('http://127.0.0.1:8000/user/', {
      headers: {
        Authorization: `Bearer ${accessToken}`
      }
    });
      artists.value = response.data;
    } catch (error) {
      console.error('Error fetching artists:', error);
    }
  });


  </script>
  
  <style scoped>
 
  </style>
  