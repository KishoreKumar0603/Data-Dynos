import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import "../css/auth.css";

const Signup = () => {
    const [formData, setFormData] = useState({
        username: "",
        aadhaarNumber: "",
        phoneNumber: "",
        city: "",
        password: "",
        confirmPassword: ""
    });

    const [message, setMessage] = useState("");
    const navigate = useNavigate();

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        
        if (formData.password !== formData.confirmPassword) {
            setMessage("Passwords do not match!");
            return;
        }

        try {
            const response = await axios.post("http://127.0.0.1:8000/api/accounts/register/", {
                username: formData.username,
                aadhaar_number: formData.aadhaarNumber,
                phone_number: formData.phoneNumber,
                city: formData.city,
                password: formData.password
            });

            if (response.status === 201) {
                setMessage("Registration successful! Redirecting...");
                setTimeout(() => navigate("/login"), 2000); // Redirect after success
            }
        } catch (error) {
            setMessage("Error registering user. Please try again.");
        }
    };

    return (
        <div className="container" id="signup">
            <div className="row p-4">
                <div className="col-md-12" id="signupcon">
                    <h2 className="text-center pb-4">SignUp</h2>
                    <form onSubmit={handleSubmit}>
                        <label>Username:</label>
                        <input type="text" name="username" placeholder="Name as Per Aadhaar" required onChange={handleChange} />

                        <label>Aadhaar Number:</label>
                        <input type="text" name="aadhaarNumber" placeholder="Aadhaar Number" required onChange={handleChange} />

                        <label>Phone Number:</label>
                        <input type="text" name="phoneNumber" placeholder="Phone Number" required onChange={handleChange} />

                        <label>City:</label>
                        <input type="text" name="city" placeholder="City" required onChange={handleChange} />

                        <label>Password:</label>
                        <input type="password" name="password" placeholder="Password" required onChange={handleChange} />

                        <label>Confirm Password:</label>
                        <input type="password" name="confirmPassword" placeholder="Confirm Password" required onChange={handleChange} />

                        <div className="text-center pt-2">
                            <button className="btn mb-1 text-center" type="submit">SIGNUP</button>
                            <p>Already have an Account? <a href="/login">LOGIN</a></p>
                            <p>{message}</p>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    );
};

export default Signup;
