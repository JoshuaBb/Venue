// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: address.proto

package address.proto;

public final class AddressOuterClass {
  private AddressOuterClass() {}
  public static void registerAllExtensions(
      com.google.protobuf.ExtensionRegistryLite registry) {
  }

  public static void registerAllExtensions(
      com.google.protobuf.ExtensionRegistry registry) {
    registerAllExtensions(
        (com.google.protobuf.ExtensionRegistryLite) registry);
  }
  static final com.google.protobuf.Descriptors.Descriptor
    internal_static_Coordinate_descriptor;
  static final 
    com.google.protobuf.GeneratedMessageV3.FieldAccessorTable
      internal_static_Coordinate_fieldAccessorTable;
  static final com.google.protobuf.Descriptors.Descriptor
    internal_static_Address_descriptor;
  static final 
    com.google.protobuf.GeneratedMessageV3.FieldAccessorTable
      internal_static_Address_fieldAccessorTable;
  static final com.google.protobuf.Descriptors.Descriptor
    internal_static_GetAddressRequest_descriptor;
  static final 
    com.google.protobuf.GeneratedMessageV3.FieldAccessorTable
      internal_static_GetAddressRequest_fieldAccessorTable;
  static final com.google.protobuf.Descriptors.Descriptor
    internal_static_GetAddressResponse_descriptor;
  static final 
    com.google.protobuf.GeneratedMessageV3.FieldAccessorTable
      internal_static_GetAddressResponse_fieldAccessorTable;
  static final com.google.protobuf.Descriptors.Descriptor
    internal_static_HelloWorldRequest_descriptor;
  static final 
    com.google.protobuf.GeneratedMessageV3.FieldAccessorTable
      internal_static_HelloWorldRequest_fieldAccessorTable;
  static final com.google.protobuf.Descriptors.Descriptor
    internal_static_HelloWorldResponse_descriptor;
  static final 
    com.google.protobuf.GeneratedMessageV3.FieldAccessorTable
      internal_static_HelloWorldResponse_fieldAccessorTable;

  public static com.google.protobuf.Descriptors.FileDescriptor
      getDescriptor() {
    return descriptor;
  }
  private static  com.google.protobuf.Descriptors.FileDescriptor
      descriptor;
  static {
    java.lang.String[] descriptorData = {
      "\n\raddress.proto\"1\n\nCoordinate\022\020\n\010latitud" +
      "e\030\001 \001(\001\022\021\n\tlongitude\030\002 \001(\001\"\376\001\n\007Address\022\027" +
      "\n\naddress_id\030\001 \001(\005H\000\210\001\001\022\017\n\007address\030\002 \001(\t" +
      "\022\014\n\004city\030\003 \001(\t\022\031\n\021state_or_province\030\004 \001(" +
      "\t\022\024\n\014country_code\030\005 \001(\t\022\025\n\010latitude\030\006 \001(" +
      "\001H\001\210\001\001\022$\n\ncoordinate\030\007 \001(\0132\013.CoordinateH" +
      "\002\210\001\001\022\025\n\010place_id\030\010 \001(\tH\003\210\001\001B\r\n\013_address_" +
      "idB\013\n\t_latitudeB\r\n\013_coordinateB\013\n\t_place" +
      "_id\"\023\n\021GetAddressRequest\"1\n\022GetAddressRe" +
      "sponse\022\033\n\taddresses\030\001 \003(\0132\010.Address\"/\n\021H" +
      "elloWorldRequest\022\021\n\004name\030\001 \001(\tH\000\210\001\001B\007\n\005_" +
      "name\"&\n\022HelloWorldResponse\022\020\n\010greeting\030\001" +
      " \001(\t2I\n\016AddressService\0227\n\014GetAddresses\022\022" +
      ".GetAddressRequest\032\023.GetAddressResponse2" +
      "L\n\021HelloWorldService\0227\n\010SayHello\022\022.Hello" +
      "WorldRequest\032\023.HelloWorldResponse(\0010\001B\021\n" +
      "\raddress.protoP\001b\006proto3"
    };
    descriptor = com.google.protobuf.Descriptors.FileDescriptor
      .internalBuildGeneratedFileFrom(descriptorData,
        new com.google.protobuf.Descriptors.FileDescriptor[] {
        });
    internal_static_Coordinate_descriptor =
      getDescriptor().getMessageTypes().get(0);
    internal_static_Coordinate_fieldAccessorTable = new
      com.google.protobuf.GeneratedMessageV3.FieldAccessorTable(
        internal_static_Coordinate_descriptor,
        new java.lang.String[] { "Latitude", "Longitude", });
    internal_static_Address_descriptor =
      getDescriptor().getMessageTypes().get(1);
    internal_static_Address_fieldAccessorTable = new
      com.google.protobuf.GeneratedMessageV3.FieldAccessorTable(
        internal_static_Address_descriptor,
        new java.lang.String[] { "AddressId", "Address", "City", "StateOrProvince", "CountryCode", "Latitude", "Coordinate", "PlaceId", "AddressId", "Latitude", "Coordinate", "PlaceId", });
    internal_static_GetAddressRequest_descriptor =
      getDescriptor().getMessageTypes().get(2);
    internal_static_GetAddressRequest_fieldAccessorTable = new
      com.google.protobuf.GeneratedMessageV3.FieldAccessorTable(
        internal_static_GetAddressRequest_descriptor,
        new java.lang.String[] { });
    internal_static_GetAddressResponse_descriptor =
      getDescriptor().getMessageTypes().get(3);
    internal_static_GetAddressResponse_fieldAccessorTable = new
      com.google.protobuf.GeneratedMessageV3.FieldAccessorTable(
        internal_static_GetAddressResponse_descriptor,
        new java.lang.String[] { "Addresses", });
    internal_static_HelloWorldRequest_descriptor =
      getDescriptor().getMessageTypes().get(4);
    internal_static_HelloWorldRequest_fieldAccessorTable = new
      com.google.protobuf.GeneratedMessageV3.FieldAccessorTable(
        internal_static_HelloWorldRequest_descriptor,
        new java.lang.String[] { "Name", "Name", });
    internal_static_HelloWorldResponse_descriptor =
      getDescriptor().getMessageTypes().get(5);
    internal_static_HelloWorldResponse_fieldAccessorTable = new
      com.google.protobuf.GeneratedMessageV3.FieldAccessorTable(
        internal_static_HelloWorldResponse_descriptor,
        new java.lang.String[] { "Greeting", });
  }

  // @@protoc_insertion_point(outer_class_scope)
}
