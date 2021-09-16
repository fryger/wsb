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

export const getters = {
  searchDriver: state => f => {
    return state.list.filter(
      r =>
        r.email.toLowerCase().includes(f) ||
        r.username.toLowerCase().includes(f) ||
        r.first_name.toLowerCase().includes(f) ||
        r.last_name.toLowerCase().includes(f)
    );
  },
  idDriver: state => id => {
    try {
      return state.list.filter(driver => driver.id == id)[0]["username"];
    } catch (e) {
      return "";
    }
  }
};
