import axios from "axios";

export const state = () => ({
  list: []
});

export const mutations = {
  SET(state, payload) {
    state.list = [];
    state.list.push(...payload);
  }
};

export const actions = {
  async getDriver({ commit }) {
    await this.$axios
      .get("/drivers")
      .then(response => commit("SET", response.data));
  }
};
