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
  async getLatestStatus({ commit }) {
    await this.$axios
      .get("/cars/latest")
      .then(response => commit("SET", response.data));
  }
};
