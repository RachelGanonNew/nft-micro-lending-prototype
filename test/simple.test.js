const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("Simple Test", function() {
  it("Should return the right greeting", async function() {
    try {
      console.log("Getting signers...");
      const [owner] = await ethers.getSigners();
      console.log("Owner address:", owner.address);
      
      console.log("Getting contract factory...");
      const Greeter = await ethers.getContractFactory("Greeter");
      console.log("Deploying contract...");
      const greeter = await Greeter.deploy("Hello, Hardhat!");
      
      const greeterAddress = greeter.address;
      console.log("Contract deployed to:", greeterAddress);
      
      console.log("Calling greet()...");
      const greeting = await greeter.greet();
      console.log("Greeting:", greeting);
      
      expect(greeting).to.equal("Hello, Hardhat!");
    } catch (error) {
      console.error("Test failed:", error);
      throw error;
    }
  });
});
