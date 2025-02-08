import { useContext } from "react";
import { Navigate } from "react-router-dom";
import AuthContext from "../context/AuthContext";

export default function Dashboard(){
    const { user, logout } = useContext(AuthContext);

    if (!user) return <Navigate to="/login" />;

    return (
        <div>
            <h2>Welcome, {user.email}!</h2>
            <button onClick={logout}>Logout</button>
        </div>
    )
}

