package address.rpc.transformer;

import address.proto.Address;

public class AddressTransformer {
    public static Address toGrpc(dao.jooq.tables.pojos.Address dao){
        return Address.newBuilder()
                .setAddressId(dao.getAddressId())
                .setAddress(dao.getAddressLineOne())
                .setCity(dao.getCity())
                .setStateOrProvince(dao.getStateOrProvince())
                .setCountryCode(dao.getCountryCode())
                .setCoordinate(CoordinateTransformer.toGrpc(dao.getLatitude().doubleValue(), dao.getLongitude().doubleValue()))
                .setPlaceId(dao.getPlaceId())
                .build();


    }
}
