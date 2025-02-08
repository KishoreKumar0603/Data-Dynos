import "../css/auth.css"

const Signup = () => {
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
