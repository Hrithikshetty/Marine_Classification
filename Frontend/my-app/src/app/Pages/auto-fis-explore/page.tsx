import { Button } from "@/components/ui/button"

export default function Component() {
  return (
    <div className="w-full py-6">
      <div className="container flex flex-col gap-4 px-4 md:px-6">
        <div className="flex flex-col gap-2">
          <h1 className="text-3xl font-bold">Auto-Fis Image Analyzer</h1>
          <p className="max-w-[600px] text-gray-500 md:text-base/relaxed dark:text-gray-400">
            Analyze an Fish image with a pre-trained machine learning model.
          </p>
        </div>
        <div className="flex flex-col gap-2">
          <div className="border border-dashed border-gray-200 border-gray-200 rounded-lg bg-white w-full p-6 flex flex-col items-center gap-2 border-gray-200 shadow-sm transition-colors hover:border-gray-300 focus-within:outline-none focus-within:border-gray-300 dark:border-gray-800 dark:border-gray-800">
            <img
              alt="Image"
              className="aspect-square object-cover rounded-lg border border-gray-200 border-gray-200 dark:border-gray-800 dark:border-gray-800"
              height="200"
              src="/placeholder.svg"
              width="200"
            />
            <p className="text-sm text-gray-500 dark:text-gray-400">Drag and drop your image here</p>
            <label
              className="inline-flex text-white h-8 items-center rounded-md border border-dashed border-gray-200 border-gray-200 bg-gray-50 px-4 text-sm font-medium shadow-sm cursor-pointer transition-colors hover:bg-gray-100 hover:text-gray-900 dark:border-gray-800 dark:border-gray-800 dark:bg-gray-950 dark:hover:bg-gray-800 dark:hover:text-gray-50"
              htmlFor="file-upload"
            >
              <input className="sr-only " id="file-upload" type="file" />
              Browse
            </label>
          </div>
          <div className="flex items-center gap-4">
            <Button className="w-32 h-8" variant="outline">
              Clear Image
            </Button>
            <Button className="w-32">Submit</Button>
          </div>
          <div className="flex flex-col gap-2">
            <h3 className="text-lg font-medium">Results</h3>
            <div className="grid gap-2">
              <div className="flex items-center gap-4">
                <div className="font-bold w-20">Prediction:</div>
                <div className="text-sm text-gray-500 dark:text-gray-400">Placeholder prediction</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

