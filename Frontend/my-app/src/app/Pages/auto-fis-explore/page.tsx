// "use client"
// import Link from "next/link";
// import { ChangeEvent, useState, useEffect } from "react";
// import { Button } from "@/components/ui/button";
// import LoadingBar from 'react-top-loading-bar'
// import { css } from '@emotion/react';
// import "./app.css";

// export default function ImageAnalyzerPage() {
//   const [image, setImage] = useState<string | null>(null);
//   const [prediction, setPrediction] = useState<string>("");
//   // const [progress, setProgress] = useState(0)

//   const handleImageUpload = (event: ChangeEvent<HTMLInputElement>) => {
//     const inputElement = event.target as HTMLInputElement;
//     if (inputElement.files && inputElement.files.length > 0) {
//       const selectedImage: File = inputElement.files[0];
//       const reader = new FileReader();
//       reader.onload = () => {
//         const imageDataUrl: string | null = reader.result as string | null;
//         setImage(imageDataUrl);
//       };
//       reader.readAsDataURL(selectedImage);
//     }
//   };
  
//   const handleClearImage = () => {
//     setImage(null);
//     setPrediction("");
//   };

//   const handleSubmit = async () => {
//     if (!image) {
//         console.error("No image selected");
//         return;
//     }

//     const formData = new FormData();
//     formData.append('file', image); 

//     try {
//         const response = await fetch("http://localhost:50603/predict", {
//             method: "POST",
//             body: formData,
//             headers: {
//                 "Content-Type": "multipart/form-data" 
//             }
//         });

//         if (response.ok) {
//             const data = await response.json();
//             setPrediction(data.message);
//         } else {
//             console.error("Failed to get prediction:", response.statusText);
//         }
//     } catch (error) {
//         console.error("Error occurred while fetching prediction:", error);
//     }
// };



//   return (
//     <>
//       <div className="h-full bg-black ">
//         <header className="h-30 py-10.5 h-5 lg:py-14.5 py-4 bg-black">
//           <div className="container grid items-center gap-4 px-4 lg:gap-8 lg:px-6 xl:px-8">
//             <Link href="#">
//               <div className="text-white flex items-center space-x-2 cursor-pointer text-black">
//                 <MountainIcon className="w-8 h-8 " />
//                 <span className="text-2xl font-bold text-white">Auto-Fis</span>
//               </div>
//             </Link>
//           </div>
//         </header>
//         <div>
//           <div className="h-30"></div>
//           <div className="w-full  flex items-center justify-center py-6 bg-black">
//             <div className="container flex flex-col gap-4 px-4 md:px-6">
//               <div className="flex flex-col gap-2">
//                 <h1 className="text-3xl font-bold text-white">
//                   Image Analyzer
//                 </h1>
//                 <p className="max-w-[600px] text-gray-500 md:text-base/relaxed dark:text-gray-400">
//                   Analyze an Fish image with a pre-trained machine learning
//                   model.
//                 </p>
//               </div>
//               <div className="flex flex-col gap-2 ">
//                 <form
//                   id="uploadForm"
//                   onSubmit={(event) => {
//                     event.preventDefault();
//                     handleSubmit();
//                   }}
//                   encType="multipart/form-data"
//                 >
//                   <div className="bg-black border border-dashed rounded-lg w-full p-6 flex flex-col items-center gap-2 border-gray-200 shadow-sm transition-colors hover:border-gray-300 focus-within:outline-none focus-within:border-gray-300 dark:border-gray-800 dark:border-gray-800">
//                     {image ? (
//                       <img
//                         alt="Uploaded Image"
//                         className="aspect-square object-cover rounded-lg border-9 bg-black"
//                         src={image}
//                       />
//                     ) : (
//                       <>
//                         <p className="text-sm text-white dark:text-gray-400">
//                           Drag and drop your image here
//                         </p>
//                         <label
//                           className="inline-flex h-8 items-center rounded-md border-30 border-dashed bg-gray-50 px-4 text-sm font-medium shadow-sm cursor-pointer transition-colors hover:bg-gray-100 hover:text-gray-900"
//                           htmlFor="file-upload"
//                         >
//                           <input
//                             className="sr-only "
//                             id="file-upload"
//                             type="file"
//                             accept="image/*"
//                             onChange={handleImageUpload}
//                           />
//                           Browse
//                         </label>
//                       </>
//                     )}
//                   </div>
//                   <div className="flex items-center gap-4 text-white">
//                     <Button
//                       className="w-32 h-8"
//                       variant="outline"
//                       onClick={handleClearImage}
//                     >
//                       Clear Image
//                     </Button>
//                     <Button type="submit" 
//                     className="flex items-center  text-white w-32"
//                     variant="outline"
//                     onClick={handleSubmit}
//                       >
//                       Submit
//                     </Button>
//                   </div>
//                 </form>
//                 <div className="flex flex-col gap-2 text-white">
//                   <h3 className="text-lg font-medium">Results</h3>
//                   <div className="grid gap-2">
//                     <div className="flex items-center gap-4">
//                       <div className="font-bold w-20">Prediction:</div>
//                       <div className="text-sm text-gray-500 dark:text-gray-400">
//                         {prediction}
//                       </div>
//                     </div>
//                   </div>
//                 </div>
//               </div>
//             </div>
//           </div>
//         </div>
//       </div>
//     </>
//   );
// }

// interface MountainIconProps extends React.SVGProps<SVGSVGElement> {}

// function MountainIcon(props: MountainIconProps) {
//   return (
//     <svg
//       {...props}
//       xmlns="http://www.w3.org/2000/svg"
//       width="24"
//       height="24"
//       viewBox="0 0 24 24"
//       fill="none"
//       stroke="currentColor"
//       strokeWidth="2"
//       strokeLinecap="round"
//       strokeLinejoin="round"
//     >
//       <path d="m8 3 4 8 5-5 5 15H2L8 3z" />
//     </svg>
//   );
// }


import React from "react";

const Scan = () => {
  return (
    <div className="text-2xl font-bold">
<<<<<<< Updated upstream
      <iframe src="http://127.0.0.1:50603/" width="800" height="600"></iframe>
=======
      <iframe src="http://localhost:8501/" width="100%" height="930px" ></iframe>
>>>>>>> Stashed changes
    </div>
  );
};

export default Scan;
