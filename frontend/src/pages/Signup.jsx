import "../css/auth.css"
// import { useState, useContext } from "react";
// import { useNavigate } from "react-router-dom";
// import AuthContext from "../context/AuthContext";

// const Signup = () => {
//     const { signup } = useContext(AuthContext);
//     const navigate = useNavigate();

//     const [formData, setFormData] = useState({
//         aadhaar: "",
//         aadhaarNumber: "",
//         phoneNumber: "",
//         city: "",
//         password: "",
//         confirmPassword: "",
//     });

//     const [errors, setErrors] = useState({});

//     const handleChange = (e) => {
//         setFormData({ ...formData, [e.target.name]: e.target.value });
//     };

//     const validateForm = () => {
//         let newErrors = {};

//         if (!/^\d{12}$/.test(formData.aadhaarNumber)) {
//             newErrors.aadhaarNumber = "Aadhaar number must be 12 digits";
//         }

//         if (!/^\d{10}$/.test(formData.phoneNumber)) {
//             newErrors.phoneNumber = "Phone number must be 10 digits";
//         }

//         if (formData.password.length < 6) {
//             newErrors.password = "Password must be at least 6 characters long";
//         }

//         if (formData.password !== formData.confirmPassword) {
//             newErrors.confirmPassword = "Passwords do not match";
//         }

//         setErrors(newErrors);
//         return Object.keys(newErrors).length === 0;
//     };

//     const handleSubmit = async (e) => {
//         e.preventDefault();
//         if (!validateForm()) return;

//         await signup(formData);
//         navigate("/login");
//     };

//     return (
//         <div className="signup-container">
//             <h2>Signup</h2>
//             <form onSubmit={handleSubmit}>
//                 <input type="text" name="aadhaar" placeholder="Aadhaar (Username)" value={formData.aadhaar} onChange={handleChange} required />

//                 <input type="text" name="aadhaarNumber" placeholder="Aadhaar Number" value={formData.aadhaarNumber} onChange={handleChange} required />
//                 {errors.aadhaarNumber && <p className="error">{errors.aadhaarNumber}</p>}

//                 <input type="text" name="phoneNumber" placeholder="Phone Number" value={formData.phoneNumber} onChange={handleChange} required />
//                 {errors.phoneNumber && <p className="error">{errors.phoneNumber}</p>}

//                 <input type="text" name="city" placeholder="City" value={formData.city} onChange={handleChange} required />

//                 <input type="password" name="password" placeholder="Password" value={formData.password} onChange={handleChange} required />
//                 {errors.password && <p className="error">{errors.password}</p>}

//                 <input type="password" name="confirmPassword" placeholder="Confirm Password" value={formData.confirmPassword} onChange={handleChange} required />
//                 {errors.confirmPassword && <p className="error">{errors.confirmPassword}</p>}

//                 <button type="submit">Signup</button>
//             </form>
//         </div>
//     );
// };

// export default Signup;


// import { useState, useContext } from "react";
// import { useNavigate } from "react-router-dom";
// import AuthContext from "../context/AuthContext";

const Signup = () => {
    // const { signup } = useContext(AuthContext);
    // const navigate = useNavigate();

    // const [formData, setFormData] = useState({
    //     aadhaar: "",
    //     aadhaarNumber: "",
    //     phoneNumber: "",
    //     city: "",
    //     password: "",
    //     confirmPassword: "",
    // });

    // const [errors, setErrors] = useState({});

    // const handleChange = (e) => {
    //     setFormData({ ...formData, [e.target.name]: e.target.value });
    // };

    // const validateForm = () => {
    //     let newErrors = {};

    //     if (!/^\d{12}$/.test(formData.aadhaarNumber)) {
    //         newErrors.aadhaarNumber = "Aadhaar number must be 12 digits";
    //     }

    //     if (!/^\d{10}$/.test(formData.phoneNumber)) {
    //         newErrors.phoneNumber = "Phone number must be 10 digits";
    //     }

    //     if (formData.password.length < 6) {
    //         newErrors.password = "Password must be at least 6 characters long";
    //     }

    //     if (formData.password !== formData.confirmPassword) {
    //         newErrors.confirmPassword = "Passwords do not match";
    //     }

    //     setErrors(newErrors);
    //     return Object.keys(newErrors).length === 0;
    // };

    // const handleSubmit = async (e) => {
    //     e.preventDefault();
    //     if (!validateForm()) return;

    //     await signup(formData);
    //     navigate("/login");
    // };

    return (
        <div className="container" id="signup">
            <div className="row">
                <div className="col-md-12" id="signupcon">
                    <h2>Signup</h2>
                    <form >
                        <label htmlFor="">Username</label>
                        <input type="text" name="aadhaar" placeholder="Aadhaar (Username)" required />
                        <label htmlFor="">Username</label>

                        <input type="text" name="aadhaarNumber" placeholder="Aadhaar Number" required />
                        <label htmlFor="">Username</label>

                        <input type="text" name="phoneNumber" placeholder="Phone Number" required />
                        <label htmlFor="">Username</label>

                        <input type="text" name="city" placeholder="City" required />
                        <label htmlFor="">Username</label>

                        <input type="password" name="password" placeholder="Password" required />
                        <label htmlFor="">Username</label>

                        <input type="password" name="confirmPassword" placeholder="Confirm Password" required />

                        <button type="submit">Signup</button>
                    </form>
                </div>
            </div>

        </div>
    );
};

export default Signup;
