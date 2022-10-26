import React from "react";

function Register() {
  return (
    <div
      className="Auth-form-container"
      style={{
        backgroundImage: "url(/images/client.png)"
      }}
    >
      <form
        className="Auth-form"
        style={{
          backgroundImage: "url(/images/blueviolet.jpg)"
        }}
      >
        <div className="Auth-form-content">
          <h3 classNaaame="Auth-form-title">
            <u>Sign Up</u>
          </h3>
          <table>
            <div className="UsPa">
              <label>
                Username&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
              </label>
              <input
                type="text"
                className="one"
                placeholder="Enter Username"
                required
              />
            </div>
            <div className="UsPa">
              <label>
                Email
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
              </label>
              <input
                type="email"
                className="one"
                placeholder="Enter email address"
                required
              />
            </div>
            <div className="UsPa">
              <label>
                Password
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
              </label>
              <input
                type="password"
                className="one"
                placeholder="Enter password"
                required
              />
            </div>
            <div className="UsPa">
              <label>Confirm Password</label>
              <input
                type="password"
                className="one"
                placeholder="Enter confirm password"
                required
              />
            </div>
          </table>
          <div className="submit">
            <button type="submit" className="btn">
              Submit
            </button>
          </div>
        </div>
      </form>
    </div>
  );
}

export default Register;
