import { useState } from "react";
import axios from "axios";

const UploadIssueForm = () => {
    const [image, setImage] = useState(null);
    const [description, setDescription] = useState("");

    const handleSubmit = async (e) => {
        e.preventDefault(); // Prevent default form submission

        const formData = new FormData();
        formData.append("image", image);
        formData.append("description", description);

        try {
            const response = await axios.post("http://127.0.0.1:8000/api/upload/", formData, {
                headers: {
                    "Content-Type": "multipart/form-data",
                },
            });
            console.log("✅ Upload Successful:", response.data);
        } catch (error) {
            console.error("❌ Upload Failed:", error.response ? error.response.data : error.message);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <input type="file" onChange={(e) => setImage(e.target.files[0])} required />
            <input type="text" placeholder="Description" value={description} onChange={(e) => setDescription(e.target.value)} required />
            <button type="submit">Upload</button>
        </form>
    );
};

// Correctly export the component
export default UploadIssueForm;
