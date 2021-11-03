import Vue from "vue";

import {
  LMap,
  LTileLayer,
  LMarker,
  LPolyline,
  LLayerGroup
} from "vue2-leaflet";

Vue.component("l-map", LMap);
Vue.component("l-tile-layer", LTileLayer);
Vue.component("l-marker", LMarker);
Vue.component("l-polyline", LPolyline);
Vue.use(LLayerGroup);
