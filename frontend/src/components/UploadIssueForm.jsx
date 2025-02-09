import React, { useState } from "react";
import axios from "axios";
import "../css/uploads.css";

const UploadIssueForm = () => {
  const [image, setImage] = useState(null);
  const [description, setDescription] = useState("");
  const [preview, setPreview] = useState(null);
  const [uploadStatus, setUploadStatus] = useState("");

  const handleImageChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      setImage(file);
      setPreview(URL.createObjectURL(file));
    }
  };

  const handleUpload = async () => {
    if (!image) {
      setUploadStatus("❌ Please select an image!");
      return;
    }

    const formData = new FormData();
    formData.append("image", image);
    formData.append("description", description);

    try {
      const response = await axios.post("http://127.0.0.1:8000/api/upload/", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      if (response.status === 201 || response.status === 200) {
        setUploadStatus("✅ Upload successful! AI is processing the image.");
        console.log("Upload Response:", response.data);
      } else {
        setUploadStatus("⚠️ Unexpected response from server.");
      }
    } catch (error) {
      console.error("❌ Error uploading image:", error.response ? error.response.data : error.message);
      setUploadStatus(`❌ Upload failed: ${error.response?.data?.error || error.message}`);
    }
  };

  return (
    <div className="container mt-4" id="upload">
      <div className="row p-4">
        <div className="col-md-12" id="upcon">
          <h2>Upload an Environmental Issue</h2>
          <input
            type="file"
            accept="image/*"
            onChange={handleImageChange}
            className="form-control my-3"
          />
          {preview && (
            <img
              src={preview}
              alt="Preview"
              className="img-thumbnail mb-3"
              style={{ maxWidth: "300px" }}
            />
          )}
          <textarea className="px-3" type="text" placeholder="Description" value={description} onChange={(e) => setDescription(e.target.value)} required />
          <button className="btn btn-primary" onClick={handleUpload}>
            Upload
          </button>
          {uploadStatus && <p className="mt-3">{uploadStatus}</p>}
        </div>
      </div>
    </div>
  );
};

export default UploadIssueForm;
