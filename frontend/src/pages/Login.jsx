import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import "../css/auth.css";

const Login = ({ setAuth }) => {
    const [credentials, setCredentials] = useState({ username: "", password: "" });
    const [message, setMessage] = useState("");
    const [loading, setLoading] = useState(false);
    const navigate = useNavigate();

    const handleChange = (e) => {
        setCredentials({ ...credentials, [e.target.name]: e.target.value });
    };

    const handleLogin = async (e) => {
        e.preventDefault();
        setLoading(true);
        setMessage("");

        try {
            const response = await axios.post("http://127.0.0.1:8000/api/login/", credentials);

            if (response.status === 200) {
                const { token, user } = response.data; // Get token & user details

                // Store authentication details
                localStorage.setItem("token", token);
                localStorage.setItem("user", JSON.stringify(user));

                setAuth(true); // Notify App.jsx that user is authenticated
                navigate("/"); // Redirect to Dashboard
            }
        } catch (error) {
            if (error.response) {
                setMessage(error.response.data.message || "Invalid credentials.");
            } else {
                setMessage("Server error. Please try again.");
            }
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="container" id="login">
            <div className="row p-4">
                <div className="col-md-12" id="logincon">
                    <h2 className="text-center pb-4">Login</h2>
                    <form onSubmit={handleLogin}>
                        <label>Username:</label>
                        <input type="text" name="username" placeholder="Enter your username" required onChange={handleChange} />

                        <label>Password:</label>
                        <input type="password" name="password" placeholder="Enter your password" required onChange={handleChange} />

                        <div className="text-center pt-4">
                            <button className="btn mb-1 text-center" type="submit" disabled={loading}>
                                {loading ? "Logging in..." : "LOGIN"}
                            </button>
                            <p>Don't have an account? <a href="/signup">SIGNUP</a></p>
                            <p className="text-danger">{message}</p>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    );
};

export default Login;
