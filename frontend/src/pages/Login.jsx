import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import "../css/auth.css";

const Login = () => {
    const [credentials, setCredentials] = useState({ username: "", password: "" });
    const [message, setMessage] = useState("");
    const navigate = useNavigate();

    const handleChange = (e) => {
        setCredentials({ ...credentials, [e.target.name]: e.target.value });
    };

    const handleLogin = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post("http://127.0.0.1:8000/api/accounts/login/", credentials);

            if (response.status === 200) {
                localStorage.setItem("token", response.data.access);
                localStorage.setItem("username", response.data.username);
                setMessage("Login successful! Redirecting...");
                setTimeout(() => navigate("/dashboard"), 2000);
            }
        } catch (error) {
            setMessage("Invalid username or password.");
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

                        <div className="text-center pt-2">
                            <button className="btn mb-1 text-center" type="submit">LOGIN</button>
                            <p>Don't have an account? <a href="/signup">SIGNUP</a></p>
                            <p>{message}</p>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    );
};

export default Login;
0 