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
  async getCars({ commit }) {
    await this.$axios
      .get("/cars")
      .then(response => commit("SET", response.data));
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
