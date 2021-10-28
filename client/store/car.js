export const state = () => ({
  list: [],
  gallery: [],
  history: []
});

export const mutations = {
  SET_DATA(state, payload) {
    state.list = payload;
  },
  SET_GALLERY(state, payload) {
    state.gallery = payload;
  },
  SET_HISTORY(state, payload) {
    state.history = payload.reverse();
  }
};

export const actions = {
  async getCar({ commit }, id) {
    await this.$axios
      .get(`/cars/${id}/`)
      .then(response => commit("SET_DATA", response.data));
  },
  async getPictures({ commit }, id) {
    await this.$axios
      .get(`cars/${id}/gallery`)
      .then(response => commit("SET_GALLERY", response.data));
  },
  async getHistory({ commit }, id) {
    await this.$axios
      .get(`cars/${id}/history`)
      .then(response => commit("SET_HISTORY", response.data));
  }
};

export const getters = {
  uniqueHistory: state => {
    return state.history.filter(
      (item, index, self) =>
        index === self.findIndex(t => t.driver.id === item.driver.id)
    );
  }
};
