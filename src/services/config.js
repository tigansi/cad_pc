import axios from "axios";

export const http = axios.create({
  baseURL: "http://192.168.6.16:5000/",
});