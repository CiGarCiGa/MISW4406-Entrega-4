package com.aeroalpes.demo.controller;


import org.apache.pulsar.client.api.PulsarClientException;
import org.springframework.pulsar.core.PulsarTemplate;
import org.springframework.web.bind.annotation.*;

@RestController
public class PubController {

    private PulsarTemplate<String> pulsarTemplate;

    public PubController(PulsarTemplate<String> pulsarTemplate){
        this.pulsarTemplate = pulsarTemplate;
    }

    @PostMapping("/messages")
    public String publish(@RequestParam("topic") String topic, @RequestBody String body) throws PulsarClientException {
        try{
            this.pulsarTemplate.send(topic, body);
        }catch (Exception ex){
            return "Error:" + ex.getMessage();
        }
        return "Publicado!";
    }
}
