"use client";
import Link from "next/link";
import * as React from "react";
import { useRouter } from "next/navigation"; // Import useRouter from next/router
import { Label } from "@/components/ui/Label";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";

export default function Component() {
  const router = useRouter();

  const [email, setEmail] = React.useState("");
  const [password, setPassword] = React.useState("");
  const [isLoading, setIsLoading] = React.useState(false);
  const [error, setError] = React.useState<string | null>(null);
  const [message, setMessage] = React.useState<string | null>(null);
  const [isLoginedIn, setIsLoginedIn] = React.useState(false); // Track login status

  const handleLogin = async () => {
    try {
      setIsLoading(true);
      const response = await fetch("http://localhost:8080/api/v1/users/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ email, password }),
      });
      if (response.ok) {
        const data = await response.json();
        localStorage.setItem("token", data.token);
        router.push("/home");
        setMessage("Login successful");
        setIsLoginedIn(true);
      } else {
        setError("Login failed. Please check your credentials.");
      }
    } catch (error) {
      console.error("Login failed:", error);
      setError("An error occurred. Please try again later.");
    } finally {
      setIsLoading(false);
      setEmail("");
      setPassword("");
    }
  };

  return (
    <>
      <header className="py-10.5 h-5 lg:py-14.5 bg-black py-4">
        <div className="container grid items-center gap-4 px-4 lg:gap-8 lg:px-6 xl:px-8">
          <Link href="#">
            <div className="flex items-center space-x-2 cursor-pointer text-white">
              <MountainIcon className="w-8 h-8" />
              <span className="text-2xl font-bold text-white">Auto-fis</span>
            </div>
          </Link>
        </div>
      </header>
      <div className="min-h-screen flex items-center justify-center bg-black">
        <div className="w-full py-6 space-y-4 md:py-12 lg:space-y-6 xl:space-y-8 rounded-lg">
          <div className="mx-auto max-w-sm px-4 space-y-4">
            <div className="space-y-2 text-center">
              <h1 className="text-2xl text-white font-bold">Sign In</h1>
            </div>
            <div className="space-y-4">
              <div className="space-y-2">
                <Label htmlFor="email">Email</Label>
                <Input
                  className="rounded-white bg-white text-white"
                  id="email"
                  onChange={(e) => setEmail(e.target.value)}
                  placeholder="Enter your email"
                  required
                  type="email"
                />
              </div>
              <div className="space-y-2 text-white">
                <Label htmlFor="password">Password</Label>
                <Input
                  id="password"
                  className="bg-white text-white "
                  className="bg-white text-white"
                  onChange={(e) => setPassword(e.target.value)}
                  placeholder="Enter your password"
                  required
                  type="password"
                />
              </div>
              <Button
                onClick={handleLogin}
                className="w-full bg-white text-black"
                disabled={isLoading}
              >
                {isLoading ? "Signing In..." : "Sign In"}
              </Button>
              
              <div className="w-full flex items-center justify-center">
                <p className="text-gray-500 dark:text-gray-400">
                  Don't have an account yet?
                  <Link className="underline" href="/Pages/register">
                    Sign up
                  </Link>
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
      {error && (
        <div className="fixed inset-0 flex items-center justify-center">
          <div className="bg-white p-6 rounded-lg shadow-md">
            <p className="text-red-500">{error}</p>
            <button onClick={() => setError(null)} className="mt-4 bg-red-500 text-white px-4 py-2 rounded-md">
              Close
            </button>
          </div>
        </div>
      )}
      {message && (
        <div className="fixed inset-0 flex items-center justify-center">
          <div className="bg-white p-6 rounded-lg shadow-md">
            <p className="text-green-500">{message}</p>
            <button onClick={() => setMessage(null)} className="mt-4 bg-green-500 text-white px-4 py-2 rounded-md">
              Close
            </button>
          </div>
        </div>
      )}
    </>
  );
}

interface MountainIconProps extends React.SVGProps<SVGSVGElement> {}

function MountainIcon(props: MountainIconProps) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <path d="m8 3 4 8 5-5 5 15H2L8 3z" />
    </svg>
  );
}
