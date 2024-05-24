<template>
  <div class="min-h-screen flex">
    <Artdash />
    <div class="flex-grow p-6">
      <div class="bg-white rounded-lg p-6">
        <p class="text-3xl text-center my-10 text-lightblue">Artist Profile</p>
        <table class="w-auto border-collapse ml-64 mt-10">
          <thead>
            <tr class="border-4 border-purple text-xl text-center">
              <th class="p-3">ID</th>
              <th class="p-3">First Name</th>
              <th class="p-3">Last Name</th>
              <th class="p-3">Email</th>
              <th class="p-3">Date of Birth</th>
              <th class="p-3">Country</th>
              <th class="p-3">Bio</th>
              <th class="p-3">Gender</th>
              <th class="p-3">Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-if="artist" class="border-4 border-purple text-center">
              <td class="p-3">{{ artist.id }}</td>
              <td class="p-3">{{ artist.first_name }}</td>
              <td class="p-3">{{ artist.last_name }}</td>
              <td class="p-3">{{ artist.email }}</td>
              <td class="p-3">{{ artist.dob }}</td>
              <td class="p-3">{{ artist.country }}</td>
              <td class="p-3">{{ artist.bio }}</td>
              <td class="p-3">{{ artist.gender }}</td>
              <td class="p-3">
                <button @click="updateProfile(artist.id)"class="ring-2 ring-green hover:bg-green text-black font-bold py-2 px-4 rounded mr-2">Update</button>
                <button @click="deleteProfile(artist.id)"class="ring-2 ring-peach hover:bg-peach text-black font-bold py-2 px-4 rounded">Delete</button>
              </td>
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
import Artdash from './Artdash.vue';
import {useRouter} from 'vue-router';
const router=useRouter()
const artist = ref(null);
const loading = ref(true);
const error = ref(null);
const artistId = localStorage.getItem('userId');

onMounted(async () => {
  try {
    const accessToken = localStorage.getItem('accessToken');
    const response = await axios.get(`http://127.0.0.1:8000/user/${artistId}`, {
      headers: {
        Authorization: `Bearer ${accessToken}`
      }
    });
    artist.value = response.data;
  } catch (err) {
    console.error('Error fetching artist:', err);
    error.value = 'Failed to load artist data';
  } finally {
    loading.value = false;
  }
});
const updateProfile = (id) => {
    router.push({name:'Updatepro',params: { artistId: id }});
  };
  const deleteProfile = async (artistId) => {
  const confirmation = window.confirm("Are you sure you want to delete this artist?");
  if (confirmation) {
    try {
      const accessToken = localStorage.getItem('accessToken');
      const response = await axios.delete(`http://127.0.0.1:8000/user/${artistId}/`, {
        headers: {
          Authorization: `Bearer ${accessToken}`
        }
      });
      console.log('Artist soft deleted successfully');

    } catch (error) {
      console.error('Error soft deleting artist:', error);
    }
  } else {
    console.log("Artist deletion canceled");
  }
};
</script>

<style scoped>
</style>
