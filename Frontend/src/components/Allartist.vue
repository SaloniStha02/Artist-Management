<template>
    <div class="min-h-screen flex">
      <Admindash />
      <div class="flex-grow p-6">
        <div class="bg-white rounded-lg p-6">
          <p class="text-3xl text-center my-10  text-lightblue">Artist List</p>
          <table class="w-2/3 border-collapse ml-64 mt-10" style="table-layout: auto; width:auto;">
            <thead>
              <tr class="border-4 border-purple text-xl text-center">
                <th class="p-3">ID</th>
                <th class="p-3">Artist Name</th>
                <th class="p-3">Email</th>
                <th class="p-3">Date of Birth</th>
                <th class="p-3 ">Country</th>
                <th class="p-3 ">Bio</th>
                <th class="p-3 ">Gender</th>
                <th class="p-3 ">Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="item in artists" :key="item.id" class="border-4 border-purple text-center">
                <td class="p-3">{{ item.id }}</td>
                <td class="p-3">{{ item.first_name }} {{ item.last_name }}</td>
                <td class="p-3">{{ item.email }}</td>
                <td class="p-3">{{ item.dob }}</td>
                <td class="p-3">{{ item.country }}</td>
                <td class="p-3">{{ item.bio }}</td>
                <td class="p-3">{{ item.gender }}</td>
                <td class="p-3">
                  <button @click="updateArtist(item.id)"class="ring-2 ring-green hover:bg-green text-black font-bold py-2 px-4 rounded mr-2">Update</button>
                  <button @click="deleteArtist(item.id)" class="ring-2 ring-peach hover:bg-peach text-black font-bold py-2 px-4 rounded">Delete</button>
                </td>
              </tr>
            </tbody>
          </table>
          <button @click="addArtist"class="mt-5 ml-[77%] bg-purple py-3 px-3 rounded-lg">Add Artist</button>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import { useRouter } from 'vue-router';
  const router = useRouter();
  import axios from 'axios';
  import Admindash from './Admindash.vue';
  
  const artists = ref([]);

  onMounted(async () => {
  try {
    const accessToken = localStorage.getItem('accessToken');
    const response = await axios.get('http://127.0.0.1:8000/artist/', {
      headers: {
        Authorization: `Bearer ${accessToken}`
      }
    });
    artists.value = response.data;
  } catch (error) {
    console.error('Error fetching artists:', error);
  }
});

  const updateArtist = (id) => {
    router.push({name:'Updateart',params: { artistId: id }});
  };

  const addArtist=()=>{
    router.push({name:'Addart'});
  }
const deleteArtist = async (artistId) => {
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
      artists.value = artists.value.filter(item => item.id !== artistId);
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
  