package com.aeroalpes.demo;

import org.springframework.boot.ApplicationRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.pulsar.annotation.PulsarListener;
import org.springframework.pulsar.core.PulsarTemplate;

@SpringBootApplication
public class DemoApplication {

	public static void main(String[] args) {
		SpringApplication.run(DemoApplication.class, args);
	}

	@Bean
	ApplicationRunner runner(PulsarTemplate<String> pulsarTemplate) {
		return (args) -> pulsarTemplate.send("hello-pulsar-topic", "Hello Pulsar World!");
	}

	@PulsarListener(subscriptionName = "hello-pulsar-sub", topics = "hello-pulsar-topic")
	void listen(String message) {
		System.out.println("Message Received: " + message);
	}
}
