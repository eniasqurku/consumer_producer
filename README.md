# File Data Distributor Task

In this task you will have to write a data distribution service that forwards file data to different consumers. The different steps of the tasks are:

1. create a class "FileReader":
    * it should be able to read in a YAML file
    * it should then sort the YAML file content alphabetically by the YAML file keys
    * then it should forward the single key-value-pairs of the YAML file to the "ContentDistributor" class as single strings
    * between forwarding each line, the "FileReader" should sleep for a random number of seconds between [0, 1.0]
2. create a class "ContentDistributor":
    * it should be able to receive data from an arbitrary source
    * it should be able to forward data to several consumers (see "ConsumerTypeA" and "ConsumerTypeB" below)
    * a consumer should be able to register at the "ContentDistributor"
    * once registered a consumer should receive all NEW data messages that the "ContentDistributor" distributes
    * uses a dedicated worker-thread to forward the data to different consumers
3. create a class "ConsumerTypeA":
    * each consumer is identified by a unique id <unique_id>
    * it should be able to register at the "ContentDistributor" and receive data from it
    * every time it receives a new data packet it should process it by printing "ConsumerTypeA <unique_id>:  <data_packet_content>"
4. create a class "ConsumerTypeB":
    * identical to the "ConsumerTypeA" class
    * the <unique_id>s of both consumer classes must not overlap
    * every time it receives a new data packet it should process it by printing "ConsumerTypeB <unique_id>: <data_packet_content>"


To test your code create:
* one instance of the "FileReader" class
* one instance of the "ContentDistributor" class
* one instance of the "ConsumerTypeA" class
* one instance of the "ConsumerTypeB" class


Use the following yaml file for testing:
```
'''   
a_key: "foo"
c_key: ["b", "a", "r"]
b_key: 8
'''
```

An example output for the yaml file above could be:
```
'''
ConsumerTypeA 1: a_key "foo"
ConsumerTypeA 1: b_key 8
ConsumerTypeB 2: a_key "foo"
ConsumerTypeB 2: b_key 8
ConsumerTypeA 1: c_key ["b", "a", "r"]
ConsumerTypeB 2: c_key ["b", "a", "r"]
'''
```

