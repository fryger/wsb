export const state = () => ({
  list: [],
  gallery: []
});

export const mutations = {
  SET_DATA(state, payload) {
    state.list = payload;
  },
  SET_GALLERY(state, payload) {
    state.gallery = payload;
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
  }
};
/*
  export const getters = {
    searchDriver: state => f => {
      return state.list.filter(
        r =>
          r.email.toLowerCase().includes(f) ||
          r.username.toLowerCase().includes(f) ||
          r.first_name.toLowerCase().includes(f) ||
          r.last_name.toLowerCase().includes(f)
      );
    }
  };
  */
