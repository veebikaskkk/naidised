// Näidised on staatilised. Worker ainult serveerib faile, main peab olemas olema.
export default {
  async fetch(request, env) {
    return env.ASSETS.fetch(request);
  }
};
