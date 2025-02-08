// import { createContext, useState, useEffect } from "react";
// import axios from "axios";

// const AuthContext = createContext();

// export const AuthProvider = ({ children }) => {
//     const [user, setUser] = useState(null);
//     const [token, setToken] = useState(localStorage.getItem("token") || "");

//     useEffect(() => {
//         if (token) {
//             axios.get("http://127.0.0.1:8000/api/user/", {
//                 headers: { Authorization: `Bearer ${token}` },
//             })
//             .then(response => setUser(response.data))
//             .catch(() => logout());
//         }
//     }, [token]);

//     const login = async (email, password) => {
//         const response = await axios.post("http://127.0.0.1:8000/api/login/", { email, password });
//         localStorage.setItem("token", response.data.token);
//         setToken(response.data.token);
//         setUser(response.data.user);
//     };

//     const signup = async (email, password) => {
//         await axios.post("http://127.0.0.1:8000/api/signup/", { email, password });
//     };

//     const logout = () => {
//         localStorage.removeItem("token");
//         setToken("");
//         setUser(null);
//     };

//     return (
//         <AuthContext.Provider value={{ user, login, signup, logout }}>
//             {children}
//         </AuthContext.Provider>
//     );
// };

// export default AuthContext;
