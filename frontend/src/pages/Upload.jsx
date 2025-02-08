import React, { useState } from "react";
import axios from "axios";
import "../css/uploads.css";

const Upload = () => {
  const [image, setImage] = useState(null);
  const [preview, setPreview] = useState(null);
  const [uploadStatus, setUploadStatus] = useState("");

  const handleImageChange = (e) => {
    const file = e.target.files[0];
    setImage(file);
    setPreview(URL.createObjectURL(file));
  };

  const handleUpload = async () => {
    if (!image) {
      setUploadStatus("Please select an image!");
      return;
    }

    const formData = new FormData();
    formData.append("image", image);

    try {
      const response = await axios.post("http://127.0.0.1:8000/api/upload/", formData);
      setUploadStatus("Upload successful! AI is processing the image.");
      console.log(response.data);
    } catch (error) {
      console.error("Error uploading image:", error);
      setUploadStatus("Upload failed.");
    }
  };

  return (
    <div className="container mt-4" id="upload">
      <div className="row p-4">
        <div className="col-md-12" id="upcon">
          <h2>Upload an Environmental Issue</h2>
          <input type="file" accept="image/*" onChange={handleImageChange} className="form-control my-3" />
          {preview && <img src={preview} alt="Preview" className="img-thumbnail mb-3" style={{ maxWidth: "300px" }} />}
          <button className="btn btn-primary" onClick={handleUpload}>
            Upload
          </button>
          {uploadStatus && <p className="mt-3">{uploadStatus}</p>}
        </div>

      </div>

    </div>
  );
};

export default Upload;
