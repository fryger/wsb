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

export const getters = {
  searchCar: state => f => {
    return state.list.filter(
      r =>
        r.body.toLowerCase().includes(f) ||
        r.name.toLowerCase().includes(f) ||
        r.manufacturer.toLowerCase().includes(f) ||
        r.model.toLowerCase().includes(f) ||
        r.fuel.toLowerCase().includes(f) ||
        r.vin.toLowerCase().includes(f) ||
        r.plate.toLowerCase().includes(f) ||
        r.status.toLowerCase().includes(f)
    );
  }
};
