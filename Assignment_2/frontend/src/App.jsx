import React, { useState } from 'react';
import './App.css'

/*
* Written by: Pruthvik Sheth
*/
function App() {
  const [content, setContent] = useState('');
  const [post, setPost] = useState(null);
  const [error, setError] = useState('');

  // Creating a post
  const createPost = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5000/post', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ content }),
      });

      if (!response.ok) {
        throw new Error('Error creating post');
      }

      const data = await response.json();
      console.log(data);
      setPost(data);
      setError('');
    } catch (err) {
      setError('Error creating post');
    }
  };

  // Retrieving a post
  const retrievePost = async () => {
    if (!post) {
      setError('No post to retrieve');
      return;
    }

    try {
      const response = await fetch(`http://127.0.0.1:5000/retrieve/${post.id}`, {
        method: 'GET',
      });

      if (!response.ok) {
        throw new Error('Error retrieving post');
      }

      const data = await response.json();
      setPost(data);
      setError('');
    } catch (err) {
      setError('Error retrieving post');
    }
  };

  // Deleting a post
  const deletePost = async () => {
    if (!post) {
      setError('No post to delete');
      return;
    }

    try {
      const response = await fetch(`http://127.0.0.1:5000/delete/${post.id}`, {
        method: 'DELETE',
      });

      if (!response.ok) {
        throw new Error('Error deleting post');
      }

      setPost(null);
      setError('');
    } catch (err) {
      setError('Error deleting post');
    }
  };

  return (
    <div className="app-container">
      <h1 className="app-title">Mastodon API Integration</h1>
      <div className="post-box">
        <textarea
          value={content}
          onChange={(e) => setContent(e.target.value)}
          placeholder="What's on your mind?"
          className="post-textarea"
        />
        <div className="button-group">
          <button onClick={createPost} className="post-button">
            Post
          </button>
          <button onClick={retrievePost} className="retrieve-button">
            Retrieve
          </button>
          <button onClick={deletePost} className="delete-button">
            Delete
          </button>
        </div>
      </div>
      {post && (
        <div className="post-display">
          <h2>Current Post</h2>
          <p>{post.content}</p>
        </div>
      )}
      {error && <p className="error-message">{error}</p>}
    </div>
  );
}

export default App;