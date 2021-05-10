import http from "./http-common";
class testApiService {
  getData() {
    return http.get("test-end");
  }
  postData(data) {
    return http.post("test-end", data);
  }
}

export default new testApiService();
