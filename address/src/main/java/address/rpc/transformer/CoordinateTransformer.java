package address.rpc.transformer;

import address.proto.Coordinate;

public class CoordinateTransformer {
    public static Coordinate toGrpc(Double lat, Double lon){
        return Coordinate.newBuilder()
                .setLatitude(lat)
                .setLongitude(lon)
                .build();
    }
}
