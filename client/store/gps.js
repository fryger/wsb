export const state = () => ({
  list: [],
  interval: []
});

export const mutations = {
  SET(state, payload) {
    state.list = payload;
  },
  SET_INTERVAL(state, payload) {
    state.interval = payload;
  }
};

export const actions = {
  async getLatestPoint({ commit }, id) {
    await this.$axios
      .get(`/cars/${id}/gps/latest`)
      .then(response => commit("SET", response.data));
  }
};
