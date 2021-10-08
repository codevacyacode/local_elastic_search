<template>
  <div class = "container">
    <h1>Добро пожаловать!</h1>
    <input type="text" v-model="query0" placeholder="Что искать?" size=80 align="center"/>
    <button type="button" class="btn btn-primary" v-on:click="sendQuery">Найти</button>
    <p>Максимальное число исправлений
    <input type="radio" id="er0" v-model="fuzziness" name="fuzziness" value="0">
    <label for="er0">0</label>
    <input type="radio" id="er1" v-model="fuzziness" name="fuzziness" value="1">
    <label for="er1">1</label>
    <input type="radio" id="er2" v-model="fuzziness" name="fuzziness" value="2">
    <label for="er2">2</label>
    <input type="radio" id="era" v-model="fuzziness" name="fuzziness" value="AUTO">
    <label for="era">по умолчанию</label></p>
    <div class="row justify-content-md-center">
      <div class="col-md-auto">
        <hr>
        <table class="table table-hover">
          <thead>
            <tr>
			  <th scope="col"> </th>
              <th scope="col"> </th>
              <th scope="col"> </th>
              <th scope="col"> </th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="doc in docs">
              <td>{{ doc.Номер }}</td>
              <td>{{ doc.Название }}</td>
              <td>{{ doc.Дата }}</td>
              <td>{{ doc.Текст }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      payload: {
        query0: '',
        fuzziness: '',
      },
      docs: [],
    };
  },
  methods: {
    sendQuery() {
      const path = 'http://localhost:5000/search';
      const payload = {
        query0: this.query0,
        fuzziness: this.fuzziness,
      };
      axios.post(path, payload)
        .then(() => {
          this.getDocs(payload);
        })
        .catch((error) => {
          // eslint-отключение следующей строки
          console.log(error);
        });
    },
    getDocs(payload) {
      const path = 'http://localhost:5000/search';
      axios.post(path, payload)
        .then((res) => {
          this.docs = res.data;
        })
        .catch((error) => {
          // eslint-отключение следующей строки
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>
