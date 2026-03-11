import grpc from "@grpc/grpc-js";
import protoLoader from "@grpc/proto-loader";

const packageDefinition = protoLoader.loadSync(
  "../../../../../proto/library.proto"
);

const proto = grpc.loadPackageDefinition(packageDefinition).library;

const client = new proto.LibraryService(
  "localhost:50051",
  grpc.credentials.createInsecure()
);

export async function GET() {
  return new Promise((resolve, reject) => {

    client.ListBooks({ page: 0, page_size: 20 }, (err, response) => {

      if (err) {
        resolve(Response.json({ error: err.message }));
        return;
      }

      resolve(Response.json(response));
    });

  });
}