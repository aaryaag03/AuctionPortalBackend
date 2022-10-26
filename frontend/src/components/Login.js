import React from "react";

function Login() {
  return (
    <div
      className="Auth-form-container"
      style={{
        backgroundImage: "url(/images/client.png)"
      }}
    >
      <form
        id="log"
        className="Auth-form"
        style={
          {
            // backgroundImage: "url(/images/blueviolet.jpg)"
          }
        }
      >
        <div className="Auth-form-content">
          <h3 classNaaame="Auth-form-title">
            <u>Sign In</u>
          </h3>
          <div className="UsPa">
            <label>Username </label>
            <input type="text" className="one" placeholder="Enter Username" />
          </div>
          <div className="UsPa">
            <label>Password &nbsp;</label>
            <input
              type="password"
              className="one"
              placeholder="Enter password"
            />
          </div>
          <div className="submit">
            <button type="submit" className="btn">
              Submit
            </button>
          </div>
          <p className="forgot">
            <a href="#">Forgot password?</a>
          </p>
        </div>
      </form>
    </div>
  );
}

export default Login;
