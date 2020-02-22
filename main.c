#include<stdio.h>
#include<netinet/in.h>
#include<sys/types.h>
#include<sys/socket.h>
#include<netdb.h>
#include<stdlib.h>
#include<string.h>

#define MAX 80
#define PORT 5000
#define SA struct sockaddr

void func(int sockfd)
{
	char buff[MAX];
	int n,count =0,nu = 2;
	
	FILE *fp;
	
    char filename[100] = "received_data.csv";
	fp=fopen(filename,"w+");
	
	fprintf(fp,"Date, Mean\n");
						
			
	for(;;)
	{
		bzero(buff,MAX);
		int n = read(sockfd,buff,sizeof(buff));
		buff[n-1] = '\0';
		
		if(count == 0)
		{
				printf("\nDATA FROM MOBILE PHONE:\n\n");
				//printf("%s \n",buff);
				count++;
				nu++;
				if(nu % 2 != 0){
					printf("%s,",buff);
					fprintf(fp,"%s,",buff);
				}
				
				else if (nu % 2 == 0){
					//printf("DATA1 : %s\n",data1);
					printf("%s\n",buff);
					fprintf(fp,"%s\n",buff);
				}
		}
		else
		{
			//printf("%s \n",buff);
		
			nu++;
			if(nu % 2 != 0){
				printf("%s,",buff);
				fprintf(fp,"%s,",buff);
			}
			
			else{
				//printf("DATA1 : %s\n",data1);
				printf("%s\n",buff);
				fprintf(fp,"%s\n",buff);
			}
		}
				
		/*
		bzero(buff,MAX);
		n=0;
		while((buff[n++]=getchar())!='\n');
		write(sockfd,buff,sizeof(buff));
		if(strncmp("exit",buff,4)==0)
		{
			printf("Server Exit...\n");
			break;
		}
		*/
	}
}

int main()
{
	int sockfd,connfd,len;
	struct sockaddr_in servaddr,cli;
	sockfd=socket(AF_INET,SOCK_STREAM,0);
	if(sockfd==-1)
	{
		//printf("socket creation failed...\n");
		exit(0);
	}
	else
		//printf("Socket successfully created..\n");
	bzero(&servaddr,sizeof(servaddr));
	servaddr.sin_family=AF_INET;
	servaddr.sin_addr.s_addr=htonl(INADDR_ANY);
	servaddr.sin_port=htons(PORT);
	if((bind(sockfd,(SA*)&servaddr, sizeof(servaddr)))!=0)
	{
		//printf("socket bind failed...\n");
		exit(0);
	}
	else
	//printf("Socket successfully binded..\n");
	if((listen(sockfd,5))!=0)
	{
		//printf("Listen failed...\n");
		exit(0);
	}
	else
		//printf("Server listening..\n");
	len=sizeof(cli);
	connfd=accept(sockfd,(SA *)&cli,&len);
	if(connfd<0)
	{
		//printf("server acccept failed...\n");
		exit(0);
	}
	else
		printf("Mobile Phone Connected to Fog Node..\n");
	func(connfd);
	close(sockfd);
}