export const state = () => ({
  list: [],
  points: []
});

export const mutations = {
  SET_POINT(state, payload) {
    state.list = payload;
  },
  SET_POINTS(state, payload) {
    state.points = payload;
  }
};

export const actions = {
  async getLatestPoint({ commit }, id) {
    await this.$axios
      .get(`/cars/${id}/gps/latest`)
      .then(response => commit("SET_POINT", response.data));
  },
  async getPointsRange({ commit }, payload) {
    await this.$axios
      .get(`/cars/${payload.id}/gps?from=${payload.from}&to=${payload.to}`)
      .then(response => commit("SET_POINTS", response.data));
  }
};

export const getters = {
  filterPoints: state => f => {}
};
